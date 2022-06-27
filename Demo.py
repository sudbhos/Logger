from log import logger

try:
    a=int(input("Please enter the first value:"))
    b=int(input("Please enter the second value:"))
    c=a%b
    # logger.info("Output:{}",format(str(c)))
except OSError as e:
    # print("Error: %s : %s" %(c,e.strerror))
    logger.info(f"Exception Raised:{str(e)}")