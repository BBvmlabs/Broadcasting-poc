from fastapi.responses import JSONResponse
from fastapi import HTTPException

async def response_valid(code,message,data):
    return JSONResponse(status_code=code,content={
        "code": code,
        "message": message,
        "data": data
    })

async def response_wrong(code,message,detials):
    return JSONResponse(status_code=code,content={
        "code": code,
        "message": message,
        "data": {
            "detials": detials
        }
    })

# Success Response
async def response_200(data = None):
    return JSONResponse(status_code=200, content={
        "code": 200,
        "message": "Successful",
        "data": data if data else "Success"
    })

# Resource Created
async def response_201(data = None, detials = None):
    return JSONResponse(status_code=201, content={
        "code": 201,
        "message": "Created Successfully",
        "data": {"detials": detials} if detials else data if data else "Created"
    })

# Delete successful
async def response_204():
    return JSONResponse(status_code=204, content=None)

# DB rollback Error
async def response_400(data = None):
    raise HTTPException(status_code=400, detail={
        "code":400,
        "message":"Bad Request",
        "data":{
            "detials": data if data else "Invalid Operation, DB in Rollback"
        }
    })

# Unauthorized - Invalid Token
async def response_401(data = None):
    return JSONResponse(status_code=401, content={
        "code": 401,
        "message": "Unauthorized",
        "data": {
            "details": data if data else "Invalid User"
        }
    })

# Payment Required - Subscription Needed
async def response_402(data = None):
    return JSONResponse(status_code=402, content={
        "code": 402,
        "message": "Payment Required",
        "data": {
            "details": data if data else "User is not subscribed"
        }
    })

# Forbidden - Access Denied
async def response_403(data = None):
    return JSONResponse(status_code=403, content={
        "code": 403,
        "message": "Forbidden",
        "data": {
            "details": data if data else "Not Authorized"
        }
    })

# Not Found - Data Does Not Exist
async def response_404(data = None, detials = None):
    return JSONResponse(status_code=404, content={ 
        "code": 404,
        "message": "Not Found",
        "data": {
            "details": detials if detials else f"Requested data not found in {data}"
        }
    })

# Conflict - Data Already Exists
async def response_409(data = None, detials = None):
    return JSONResponse(status_code=409, content={
        "code": 409,
        "message": "Conflict",
        "data": {"detials": detials} if detials else data
    })

# Internal Server Error
async def response_500(error_message):
    raise HTTPException(status_code=500, detail={
        "code": 500,
        "message": "Internal Server Error",
        "data": {
            "details": f"{error_message}"
        }
    })

async def response_503():
    return JSONResponse(status_code=503, content={
        "code": 503,
        "message": "Service Unavailable",
        "data": {
            "details": "Notification Service is Not Running"
        }
    })

# Custom response
async def custom_response(code,data):
    return JSONResponse(status_code=code, content=data)

# Custom Error
async def Custom_error(error):
    return JSONResponse(status_code=error["code"], content=error)