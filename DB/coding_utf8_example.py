# coding:utf-8

'''
Created on Dec 3, 2016

@author: Bin Liang
'''


def run_main():
    """
        main function
    """
    chinese_str = 'Python数据分析'
    print chinese_str

    other_str = 'naïve'
    print other_str

    nums=['a',1,2]
    tp=('a',1,2)
    print nums.__sizeof__()
    print tp.__sizeof__()

if __name__ == '__main__':
    run_main()