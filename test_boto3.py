import boto3
import json
import datetime
import dateutil.parser  
import decimal  
  
CONVERTERS = {  
    'datetime': dateutil.parser.parse,  
    'decimal': decimal.Decimal,  
}  
  
  
class MyJSONEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, (datetime.datetime,)):  
            #return {"val": obj.isoformat(), "_spec_type": "datetime"} 
            return obj.isoformat()
        elif isinstance(obj, (decimal.Decimal,)):  
            #return {"val": str(obj), "_spec_type": "decimal"}  
            return str(obj)
        else:  
            return super().default(obj)  
  
  
'''def object_hook(obj):  
    _spec_type = obj.get('_spec_type')  
    if not _spec_type:  
        return obj  
  
    if _spec_type in CONVERTERS:  
        return CONVERTERS[_spec_type](obj['val'])  
    else:  
        raise Exception('Unknown {}'.format(_spec_type))  
'''
#s3 = boto3.resource('s3')

#for bucket in s3.buckets.all():
#    print(bucket.name)
    

client = boto3.client('elasticache')

output_dict=client.describe_cache_clusters()


#print(client.describe_cache_clusters())
#print(client.describe_cache_engine_versions())
print(output_dict)
print(json.dumps(output_dict,cls=MyJSONEncoder,indent=1))



############   ElastiCache   ############
######### client
#add_tags_to_resource()
#authorize_cache_security_group_ingress()
#can_paginate()
#copy_snapshot()
#create_cache_cluster()
#create_cache_parameter_group()
#create_cache_security_group()
#create_cache_subnet_group()
#create_replication_group()
#create_snapshot()
#delete_cache_cluster()
#delete_cache_parameter_group()
#delete_cache_security_group()
#delete_cache_subnet_group()
#delete_replication_group()
#delete_snapshot()
#describe_cache_clusters()
#describe_cache_engine_versions()
#describe_cache_parameter_groups()
#describe_cache_parameters()
#describe_cache_security_groups()
#describe_cache_subnet_groups()
#describe_engine_default_parameters()
#describe_events()
#describe_replication_groups()
#describe_reserved_cache_nodes()
#describe_reserved_cache_nodes_offerings()
#describe_snapshots()
#generate_presigned_url()
#get_paginator()
#get_waiter()
#list_allowed_node_type_modifications()
#list_tags_for_resource()
#modify_cache_cluster()
#modify_cache_parameter_group()
#modify_cache_subnet_group()
#modify_replication_group()
#purchase_reserved_cache_nodes_offering()
#reboot_cache_cluster()
#remove_tags_from_resource()
#reset_cache_parameter_group()
#revoke_cache_security_group_ingress()

######### Paginator
#ElastiCache.Paginator.DescribeCacheClusters
#ElastiCache.Paginator.DescribeCacheEngineVersions
#ElastiCache.Paginator.DescribeCacheParameterGroups
#ElastiCache.Paginator.DescribeCacheParameters
#ElastiCache.Paginator.DescribeCacheSecurityGroups
#ElastiCache.Paginator.DescribeCacheSubnetGroups
#ElastiCache.Paginator.DescribeEngineDefaultParameters
#ElastiCache.Paginator.DescribeEvents
#ElastiCache.Paginator.DescribeReplicationGroups
#ElastiCache.Paginator.DescribeReservedCacheNodes
#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings
#ElastiCache.Paginator.DescribeSnapshots

######### wait
#ElastiCache.Waiter.CacheClusterAvailable
#ElastiCache.Waiter.CacheClusterDeleted
#ElastiCache.Waiter.ReplicationGroupAvailable
#ElastiCache.Waiter.ReplicationGroupDeleted