from django.shortcuts import render, HttpResponse

# Create your views here.


class Salary:
    star_doudi_dict = {
        1: 1800,
        2: 2000,
        3: 2200,
        4: 2400,
        5: 2700,
        6: 3000,
        7: 3400
    }
    ks_fee = [
        [16, 18, 21, 23, 25, 28, 30],
        [20, 22, 25, 27, 29, 32, 34],
        [25, 27, 30, 32, 34, 37, 39],
        [35, 37, 40, 42, 44, 47, 49],
        [40, 42, 45, 47, 49, 52, 54]
    ]
    def __init__(self, star_level=1, total_hour=0.0,
                 first=0.0,second=0.0,third=0.0,forth=0.0,fifth=0.0):
        self.total_hour = total_hour
        self.extra_hour = total_hour-30
        self.fee_list = self.generate_fee_list()
        self.extra_salary = self.cal_extra_salary(first,second,third,
                                                  forth, fifth)
        self.star_level = star_level

    def generate_fee_list(self):
        tmp_ks_fee = []
        for i in range(len(self.ks_fee[0])):
            tmp_list = []
            for j in range(len(self.ks_fee)):
                tmp_list.append(self.ks_fee[j][i])
            tmp_ks_fee.append(tmp_list)
        if self.extra_hour <= 60:
            return tmp_ks_fee[0]
        elif self.extra_hour <= 90:
            return tmp_ks_fee[1]
        elif self.extra_hour <= 110:
            return tmp_ks_fee[2]
        elif self.extra_hour <= 130:
            return tmp_ks_fee[3]
        elif self.extra_hour <= 150:
            return tmp_ks_fee[4]
        elif self.extra_hour <= 170:
            return tmp_ks_fee[5]
        else:
            return tmp_ks_fee[6]

    def cal_extra_salary(self, first, second, third, forth, fifth):
        cal = 0
        if first > 0:
            cal += first*self.fee_list[0]
        if second > 0:
            cal += second*self.fee_list[1]
        if third > 0:
            cal += third*self.fee_list[2]
        if forth > 0:
            cal += forth*self.fee_list[3]
        if fifth > 0:
            cal += fifth*self.fee_list[4]
        return cal

    def get_total_salary(self):
        return self.get_doudi()+self.extra_salary

    def get_doudi(self):
        return self.star_doudi_dict[self.star_level]


def get_total(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    star_level = int(request.POST.get('star_level'))
    first = eval(request.POST.get('first'))
    second = eval(request.POST.get('second'))
    third = eval(request.POST.get('third'))
    forth = eval(request.POST.get('forth'))
    fifth = eval(request.POST.get('fifth'))
    total_hour = first + second + third + forth + fifth
    salary = Salary(star_level=star_level,
                    total_hour=total_hour,
                    first=first,
                    second=second,
                    third=third,
                    forth=forth,
                    fifth=fifth,
                    )
    total_salary = salary.get_total_salary()
    return HttpResponse(total_salary)