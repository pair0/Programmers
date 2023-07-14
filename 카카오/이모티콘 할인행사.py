### 내 풀이
### 10%, 20%, 30%, 40%
### 이모티콘 플러스 가입자를 늘리기 위해서는 할인률을 최대한 낮춰야한다.
### 이모티콘 구매 비용을 올리기 위해서는 최대한 할인률을 모든 사람에게 맞추는 것이다.
def price(users, sale, emoticons):
    total_price, plus_select = 0, 0
    for user in users:
        price_num = 0
        for i in range(len(emoticons)):
            if user[0] > sale[i]:
                continue
            else:
                price_num += emoticons[i] * ((100-sale[i])/100)
                # (emoticons[i] - (emoticons[i] * (sale[i]/100)))

        if user[1] > price_num:
            total_price += price_num
        else:
            plus_select += 1
        
    return (int(total_price), plus_select)    

def solution(users, emoticons):
    answer = [-1, -1]
    users.sort()
    
    if users[0][0] <= 10:
        sale = [10, 20, 30, 40]
    elif users[0][0] <= 20:
        sale = [20, 30, 40]
    elif users[0][0] <= 30:
        sale = [30, 40]
    else:
        sale = [40]
        
    discount = []
    def dfs(tmp, d): # 모든 경우의 할인율 조합을 구함
        if d == len(tmp):
            discount.append(tmp[:])
            return
        else:
            for i in sale:
                tmp[d] += i
                dfs(tmp, d+1)
                tmp[d] -= i
    dfs([0]*len(emoticons), 0)
    
    for discounts in discount:
        price_total, plus_select = price(users, discounts, emoticons)
        if answer[0] < plus_select:
            answer = [plus_select, price_total]
        elif answer[0] == plus_select:
            if answer[1] < price_total:
                answer = [plus_select, price_total]
         
    return answer


### 다른사람 풀이
discounts = [10, 20, 30, 40]
answer = [-1, -1]

def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    discount_list = [0]*m
    
    def search(idx):
        global answer
        if idx == m :
            sale_num, cost_num = 0, 0
            for i in range(n) :
                tmp = 0
                for j in range(m) :
                    if users[i][0] <= discount_list[j] :
                        tmp += emoticons[j] * ( 100 - discount_list[j] ) // 100
                if tmp >= users[i][1] :
                    sale_num += 1
                else :
                    cost_num += tmp
            if sale_num > answer[0] or sale_num == answer[0] and cost_num > answer[1] :
                answer = [sale_num, cost_num]
            return
        
        for i in range(4) :
            discount_list[idx] = discounts[i]
            search(idx+1)
    
    search(0)
    
    return answer