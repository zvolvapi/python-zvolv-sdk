# Copyright 2024 The Zvolv Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import os
from zvolv_sdk import ZvolvClient


def handler(context, event):
    context.logger.info('Initializing Zvolv Client')
    client = ZvolvClient(os.environ['HOST'])
    
    # Initialize workspace
    workspace = client.workspace.init(os.environ['WORKSPACE'])
    
    # Authenticate user
    userinfo = client.auth.login(os.environ['USERNAME'], os.environ['PASSWORD'])

    # Start your automation from here
    

     
    # Return response
    return {}
