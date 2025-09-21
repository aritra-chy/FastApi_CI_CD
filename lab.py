from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class stock(BaseModel):
    id : int
    name : str
    description : str
    category : str
    is_Available : bool

stocks : List[stock] = []
api = FastAPI()


@api.get("/stock")
def get_stock():
    return stocks

@api.get("/stock/{stock_id}")
def get_stock(stock_id: int):
    for stock in stocks:
        if stock.id == stock_id:
            return stock
        return {"message": "stock not found"}

@api.post("/stock")
def create_stock(stock: stock):
    stocks.append(stock)
    return stocks

@api.put("/stock/{stock_id}")
def update_stock(stock_id: int, updated_stock: stock):
    for index, stock in enumerate(stocks):
        if stock.id==stock_id:
            stocks[index]=updated_stock
            return stocks
    return {"message": "error in updation"}

@api.delete("/stock/{stock_id}")
def delete_stock(stock_id: int):
    for index, stock in enumerate(stocks):
        if stock.id==stock_id:
            stocks.pop(index)
            return stocks
    return {"message": "error in deletion"}
