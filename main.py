#!/usr/bin/env python

import json

def load_data():
    holdingList = {}
    fundList = {}
    with open('data/sample-funds.json') as json_file:
        data = json.load(json_file)
        holdingList[data[0]['name']] = 1
        for item in data:
            fundList[item['name']] = {}
            for h in item['holdings']:
                fundList[item['name']][h['name']] = h['weight']
    return holdingList, fundList

def process_data_works_for_one_loop(holdingList, fundList):
    newHoldingList = {}
    print("holdingList = {!s}".format(holdingList))
    for holdings in holdingList:
        print("holdings = {!s}".format(holdings))
        if holdings in fundList:
            print("fundList = {!s}".format(fundList))
            replacementList = fundList[holdings]
            print("replacementList = {!s}".format(replacementList))
            for h in replacementList:
                print("h = {!s}".format(h))
                existingValue = 0
                if h in newHoldingList:
                    existingValue = newHoldingList[h]

                newHoldingList[h] = existingValue + (holdingList[holdings] * replacementList[h])

    print("newHoldingList = {!s}".format(newHoldingList))



def process_data(holdingList, fundList):
    newHoldingList = {}
    print("original holdingList = {!s}".format(holdingList))
    anything_replaced = False

    for holdings in holdingList:
        print("holdings = {!s}".format(holdings))
        if holdings in fundList:
            anything_replaced = True
            replacementList = fundList[holdings]
            print("replacementList = {!s}".format(replacementList))
            for replacement in replacementList:
                # print("h = {!s}".format(h))
                existingValue = 0
                if replacement in newHoldingList:
                    existingValue = newHoldingList[replacement]
                    print("found existing value for {!s} = {!s}".format(replacement, existingValue))

                newHoldingList[replacement] = existingValue + (holdingList[holdings] * replacementList[replacement])
                print("replacement {!s} = {!s}".format(replacement, newHoldingList[replacement]))
        else:
            existingValue = 0
            if holdings in newHoldingList:
                existingValue = newHoldingList[holdings]
                print("found existing value for {!s} = {!s}".format(holdings, existingValue))
            newHoldingList[holdings] = existingValue + holdingList[holdings]

        print("newHoldingList at end of loop= {!s}".format(newHoldingList))
                
    print("newHoldingList at end of function = {!s}".format(newHoldingList))
    if anything_replaced:
        return process_data(newHoldingList, fundList)
    else:
        return newHoldingList

if __name__ == '__main__':
    holdingList, fundList = load_data()
    finalList = process_data(holdingList, fundList)
    print("finalList = {!s}".format(finalList))
