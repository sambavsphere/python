str_symbol_map={'PLUS':'+','MULTIPLY':'*','DIVISION':'/'}
def evaluate(expr):
    for i in str_symbol_map.iteritems():
        expr=expr.replace(i[0],i[1])
    return eval(expr)

while True:
    print """
        1. Go for evaluation
        2. Quit
    """
    opt = raw_input("Enter an option: ")
    if opt == '1':
        qs = raw_input("enter number of questions: ")
        questions=[]
        for i in range(int(qs)):
            expr = raw_input("Enter an Expression %s:"%i)
            questions.append(expr)
        for i in questions:
            print evaluate(i)
    else:
        break
