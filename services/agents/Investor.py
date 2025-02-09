import datetime
import os
import pandas as pd
import pprint as pp
from Agent import Agent
from Analyst import Analyst
# from util import tickers
# from services.agents.Agent import Agent
# from services.agents.Analyst import Analyst
# from services.util import tickers

class Investor(Agent):
    def __init__(self, name, fund, description, investment_style, risk_tolerance, entry_criteria, exit_criteria, prompt_style, explainability_preference):
        super().__init__()
        self.tickers = ["AAPL","MSFT","META","NVDA","TSLA","AMZN","GOOG"]
        self.name = name
        self.fund = fund
        self.description = description
        self.investment_style = investment_style
        self.risk_tolerance = risk_tolerance
        self.entry_criteria = entry_criteria
        self.exit_criteria = exit_criteria
        self.prompt_style = prompt_style
        self.explainability_preference = explainability_preference
        self.balance_sheet_insights = Analyst().get_analysis()
        pp.pprint(self.balance_sheet_insights)
        self.stock_data = {
            "AAPL": None,
            "MSFT": None,
            "GOOG": None,
            "AMZN": None,
            "NVDA": None,
            "TSLA": None,
            "META": None
        }
        
        self.holdings = {
            "AAPL": 0,
            "MSFT": 0,
            "GOOG": 0,
            "AMZN": 0,
            "NVDA": 0,
            "TSLA": 0,
            "META": 0
        }

        self.get_price_data()

    # TODO: prevent negative cashafter transactions
    def generate_prompt(self, **kwargs):
        # name = kwargs.get("name", "Unknown Advisor")
        # description = kwargs.get("description", "Investment Advisor")
        # investment_style = kwargs.get("investment_style", "Balanced")
        # risk_tolerance = kwargs.get("risk_tolerance", "Moderate")
        fund = kwargs.get("fund", 0.0)
        # entry_criteria = kwargs.get("entry_criteria", "No defined criteria")
        # exit_criteria = kwargs.get("exit_criteria", "No defined criteria")
        # prompt_style = kwargs.get("prompt_style", "Professional")
        # explainability_preference = kwargs.get("explainability_preference", "High")
        # stock_data = kwargs.get("stock_data", "No data available")
        # balance_sheet_insights = kwargs.get("balance_sheet", "No balance sheet data")
        date = kwargs.get("date",str(datetime.datetime.now()))

    
        # Handle holdings safely
        holdings = kwargs.get("holdings", {})
        holdings_str = "\n".join([f"        {symbol}: {quantity} shares" for symbol, quantity in holdings.items()]) if holdings else "No holdings"

    
        return f"""You are an investment advisor with the following profile:

            NAME: {self.name}
            ROLE: {self.description}
        
            Core Characteristics:
            - Investment Style: {self.investment_style}
            - Risk Tolerance: {self.risk_tolerance}
            - Available Cash: ${fund:,.2f}
        
            Current Portfolio: {holdings_str}
        
            Decision Criteria:
            - Entry Points: {self.entry_criteria}
            - Exit Points: {self.exit_criteria}
        
            Communication Guidelines:
            - Tone: {self.prompt_style}
            - Analysis Detail: {self.explainability_preference}

            Given the stock data and current holdings above, analyze it according to your profile and provide your response in the following JSON format:
            {{
                "recommendations": [
                    {{
                        "symbol": "TICKER",
                        "action": "BUY/HOLD/SELL",
                        "quantity": number_of_shares,
                        "price_per_share": current_price,
                        "total_transaction_value": price_per_share * quantity,
                        "reasoning": "Specific reason for this recommendation"
                    }}
                ],
                "key_metrics": ["metric1", "metric2", ...],
                "analysis": "Overall market and portfolio analysis",
                "risks": ["risk1", "risk2", ...],
                "portfolio_impact": "Analysis of how these recommendations affect current positions",
                "cash_after_transactions": "Remaining cash after all recommended transactions"
            }}

            cash_after_transactions SHOULD NEVER be negative.
            Today's date is {date}. DO NOT include data future dates in the given price data, if any.

            Historical price data per company in CSV format:
            {self.stock_data}

            Balance sheet analyses by copany:
            {self.balance_sheet_insights}
            """
    
    def get_price_data(self):
        for ticker in self.tickers:
            file_name = f"historical_data_{ticker}.csv"
            with open(os.path.join(os.getcwd(),"data",file_name)) as csv:
                data = pd.read_csv(csv)
                self.stock_data[ticker] = data.to_string()

    def query(self, prompt):
        # # prompt = self.generate_prompt(
        # #     name=self.name,
        # #     description=self.description,
        # #     investment_style=self.investment_style,
        # #     risk_tolerance=self.risk_tolerance,
        # #     fund=self.fund,
        # #     entry_criteria=self.entry_criteria,
        # #     exit_criteria=self.exit_criteria,
        # #     prompt_style=self.prompt_style,
        # #     explainability_preference=self.explainability_preference,
        # #     stock_data=self.stock_data,
        # #     holdings=self.holdings
        # )
        return super().query(prompt).text

    def set_fund(self,fund):
        self.fund = fund

    def buy(self, symbol, quantity):
        self.holdings[symbol] += quantity
    
    def sell(self, symbol, quantity):
        self.holdings[symbol] -= quantity

if __name__ == "__main__":
    Buffet = Investor("Warren Buffet", 1000000, "A disciplined value investor seeking undervalued companies with strong fundamentals.", "Value", "Moderate", "P/E ratio below industry average and positive free cash flow.", "Stock price reaches target price or P/E ratio exceeds industry average.", "Formal and analytical", "Detailed explanations are required.")
    pp.pprint(Buffet.query(Buffet.generate_prompt(fund=10000.0, date="2020-09-11")))

    