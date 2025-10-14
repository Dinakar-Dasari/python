import boto3
# boto3 should present in the host
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])
    for snapshot in response['Snapshots']:
        snapshotid = snapshot["SnapshotId"]
        volumeid =  snapshot.get('VolumeId')

        if not volumeid:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshotid)
            print(f"Deleted EBS snapshot {snapshotid} as it's not attached to any volume")
        else:
            # Check if the volume still exists but not attached to any instance  
            try:
                volume_repsonse = ec2.describe_volumes(VolumeIds=[volumeid])
                if not volume_repsonse["Volumes"][0]["Attachments"]:
                    ec2.delete_snapshot(SnapshotId=snapshotid)
                    print(f"Deleted EBS snapshot {snapshotid} as it was taken from a volume not attached to any running instance.") 
            except ec2.exceptions.ClientError as e:
                 if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshotid)
                    print(f"Deleted EBS snapshot {snapshotid} as its associated volume was not found.")                         


''' 
# i can also use volumeid = snapshot['VolumeId'],
    but any snapshot doesn’t have any volume attached to it(for example, if it’s an orphan snapshot — created manually or after its volume was deleted),
    Python will raise a KeyError.
    → ❌ Your Lambda function will crash at that point. 
# in if not volume_repsonse["Volumes"][0]["Attachments"]
    if that volume is not attached to any instance, then "Attachments" becomes an empty list, not None
    If "Attachments" is an empty list ([]) → evaluates to False, meaning no attachments.
    If there’s at least one attachment (list has items) → evaluates to True, meaning volume is attached.
# Your Lambda didn’t finish executing before the timeout. This is a common issue when:
    # You’re calling AWS APIs like describe_snapshots, describe_volumes, etc., and the response takes longer than expected.
        # If you have hundreds or thousands of snapshots/volumes, this can be slow.
    # Your Lambda’s timeout setting is too low. Default is usually 3 seconds, which is clearly too short for EBS snapshot operations.
    # Sometimes network issues in Lambda can slow API calls, especially for multiple describe_volumes calls in a loop. 
    ## fix: Increase Lambda timeout --> Go to Lambda → Configuration → General configuration → Timeout → increase to 30 seconds or more.
# snapshot.get('VolumeId') always contains the ID of the volume the snapshot was created from, even if that volume has been deleted later.
    # AWS snapshots don’t lose the VolumeId when the volume is deleted.
    # So volumeid is not None → your code goes into the else branch.       
    # since, it didn't find the volumeid as we deleted & at ec2.describe_volumes(VolumeIds=[volumeid]) can’t find it → throws InvalidVolume.NotFound error.
'''