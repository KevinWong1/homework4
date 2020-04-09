import sys
import utils

try:
    command = sys.argv[1]
    if command == "build":
        print("Build was specified")
        utils.main()
    # TODO: Do something here...
    elif command == "new":
        print("New page was specified")
    # TODO: Do something here...
    else:
        print("Please specify ’build’ or ’new’ after manage.py")
except:
    print("Please specify ’build’ or ’new’ after manage.py")
