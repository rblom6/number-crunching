def lambda_handler(event, context):
    try:
        operation = int(event["queryStringParameters"]["key1"])
        firstNum = float(event["queryStringParameters"]["key2"])
        seconNum = float(event["queryStringParameters"]["key3"])
        
        if(operation == 1):
            resp = firstNum + seconNum
        elif(operation == 2):
            resp = firstNum - seconNum
        elif(operation == 3):
            resp = firstNum * seconNum
        elif(operation == 4):
            resp = firstNum / seconNum
        else:
            raise ValueError("Invalid value for operation")
            
    except:
        resp = "Invalid input"
    
    return resp