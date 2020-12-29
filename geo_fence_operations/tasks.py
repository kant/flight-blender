import plcnxdb.settings 
from celery.decorators import task
from celery.utils.log import get_task_logger
import logging
import geo_fence_rw_helper



@task(name="WriteGeoFence")
def write_geo_fence(geo_fence): 
    my_credentials = geo_fence_rw_helper.PassportCredentialsGetter()
    gf_credentials = my_credentials.get_cached_credentials()
    
    try: 
        assert any(gf_credentials) == True # Credentials dictionary is populated
    except AssertionError as ae: 
        # Error in getting a Geofence credentials getting
        logging.error('Error in getting Flight Declaration Token')
        logging.error(ae)

    my_uploader = geo_fence_rw_helper.GeoFenceUploader(credentials = gf_credentials)
    upload_status = my_uploader.upload_to_server(gf=geo_fence)

    logging.info(upload_status)