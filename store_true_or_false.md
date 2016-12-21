http://sw32.com/the-meaning-of-action-store_true-and-store_false-in-python-argparse-module/  

>If the correspond parameter does not exist, the value is opposite of store_true/store_false. If the parameter exists, the value is store_true/store_false. So we use use store_true in the most situation. return false if parameter doesn’t exist; return true if parameter exists. That’s what we want! 

```
def fun4():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--p1', action='store_true')
    parser.add_argument('--p2', action='store_true')
    parser.add_argument('--p3', action='store_false')
    cmd =  '--p1'
    args = parser.parse_args(cmd.split())
    print(args)
    if args.p1:
        print('p1 good')
    else:
        print('p1 bad')
        
    
    
print('\n========Go!==========\n')
fun4()
```