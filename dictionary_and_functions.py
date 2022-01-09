# Dictionary is nothing but a key value pairs
d1 = {}
print(type(d1))
d2 = {"Siddharth" : "Puri",
      "Satwik" : "Idlli",
      "yash" : "pizza",
      "maanav" : "samosa",
      "siddharth" : {"B" : "paratha",
                     "L" : "rice",
                     "D" : "roti"}}
d2["Ankit"] = "junk food"
d2["Aurangzeb"] = "kauchri"
del d2["Aurangzeb"]
print(d2)

d3 = d2.copy()
del d3["Siddharth"]
print(d2.get("Siddharth"))
d2.update({"Mohit" : "Toffee"})
print(d2)
print(d2.keys())
print(d2.items())
