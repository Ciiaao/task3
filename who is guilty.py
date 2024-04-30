import copy

def who_is_guilty(suspects):
    suspect_list=list(suspects.keys())
    suspect_list1=list(suspects.keys())
    speech_list=list(suspects.values())
    for guilty in suspect_list:
        new=copy.deepcopy(list(suspects.values()))
        guilty_suspect= guilty+' is'
        for speech in new:
            for i in range(3):
                if speech[i]==guilty_suspect:
                    speech[i]=True
                elif guilty_suspect+' not'==speech[i]:
                    speech[i]=False
                else:
                    pass
        for speech in new:
            for i in range(3):
                if type(speech[i])!=type(True):
                    if 'not' in speech[i]:
                        speech[i]=True
                    else:
                        speech[i]=False
        true_count=0
        false_count=0
        for speech in new:
            for x in speech:
                if x ==True:
                    true_count+=1
                else:
                    false_count+=1
        
        if true_count==6:
            print(f'{guilty} is the thief!')
            break

            

suspects={'a':[False,'b is',True],'b':['d is not','a is not','b is not'],'c':[True,'b is not',True],'d':['d is',False,'a is']}
who_is_guilty(suspects)
