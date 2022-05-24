stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25],
          ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]

sell_list = []

for symbol in stocks:
    if symbol[2] >= 5:
        sell_list.append(symbol[0])

print(sell_list)