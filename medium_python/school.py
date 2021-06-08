
def switch_demo():
    a={}
    q=0
    while q==0:


        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        try:
            i=int(input("que onda"))
            s=switcher.keys(i)
            q=1
        except ValueError:
            print("invalid month")

switch_demo()
