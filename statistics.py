#!env python3
import os
import json

ROUND_CNT = 10 # 要跑的对局数

points=[0 for i in range(4)]
wins  =[0 for i in range(4)]
blow  =[0 for i in range(4)]
if __name__ == "__main__":
    for i in range(ROUND_CNT):
        os.system("./runner -q > result.json")
        with open('result.json','r') as f:
            result=json.loads(f.read())
        print('Round %d:' % i,result)
        if result['display']['action'] not in ('HU','HUANG'):
            os.system('cp log.json '+'log.%d.json' % i)
        Min=0
        Max=0
        Player=-1
        for i in range(4):
            points[i]+=result['content'][str(i)]
            if result['content'][str(i)]>0:
                Max=result['content'][str(i)]
                wins[i]+=1
            if result['content'][str(i)]<Min:
                Min=result['content'][str(i)]
                Player=i
        if Min<0 and Min*3+Max!=0:
            blow[Player]+=1
            
    print('Statistics after %d rounds:' % ROUND_CNT)
    print('total/avg points:\t%d/%d/%d/%d\t|\t%.2f/%.2f/%.2f/%.2f' % (points[0],points[1],points[2],points[3],points[0]/ROUND_CNT,points[1]/ROUND_CNT,points[2]/ROUND_CNT,points[3]/ROUND_CNT))
    print('total/avg wins:  \t%d/%d/%d/%d\t|\t%.2f/%.2f/%.2f/%.2f'% (wins[0],wins[1],wins[2],wins[3],wins[0]/ROUND_CNT,wins[1]/ROUND_CNT,wins[2]/ROUND_CNT,wins[3]/ROUND_CNT))
    print('total/avg blow:  \t%d/%d/%d/%d\t|\t%.2f/%.2f/%.2f/%.2f'% (blow[0],blow[1],blow[2],blow[3],blow[0]/ROUND_CNT,blow[1]/ROUND_CNT,blow[2]/ROUND_CNT,blow[3]/ROUND_CNT))