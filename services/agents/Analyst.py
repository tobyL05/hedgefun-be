import json
import pprint as pp
import os
import dotenv
from services.agents.Agent import Agent
# from Agent import Agent
# from util import tickers


# python3 services/agents/Analyst.py
dotenv.load_dotenv()
key = os.getenv("DCF_API_KEY")


class Analyst(Agent):

    def __init__(self):
        super().__init__()
        self.tickers = ["AAPL","MSFT","META","NVDA","TSLA","AMZN","GOOG"]
        self.balance_sheets = {
            "MSFT": None,
            "AAPL": None,
            "GOOG": None,
            "AMZN": None,
            "NVDA": None,
            "TSLA": None,
            "META": None
        }
        self.get_balance_sheets()
    
    def get_balance_sheets(self):
        for ticker in self.tickers:
            file_name = f"balance_sheet_{ticker}.json"
            with open(os.path.join(os.getcwd(),"data",file_name)) as json_file:
                self.balance_sheets[ticker] = json.load(json_file) 
    
    def generate_prompt(self):
        prompt = f"""You are an expert investment analyst, analyzing trends in company balance sheets. An example of a balance sheet is given below for Google (GOOG), filed on the given date. All currencies will be in USD:
        {{
            "date": "2024-12-31",
            "symbol": "GOOG",
            "reportedCurrency": "USD",
            "cik": "0001652044",
            "fillingDate": "2025-02-05",
            "acceptedDate": "2025-02-04 20:41:40",
            "calendarYear": "2024",
            "period": "Q4",
            "cashAndCashEquivalents": 23466000000,
            "shortTermInvestments": 72191000000,
            "cashAndShortTermInvestments": 95657000000,
            "netReceivables": 52340000000,
            "inventory": 0,
            "otherCurrentAssets": 15714000000,
            "totalCurrentAssets": 163711000000,
            "propertyPlantEquipmentNet": 184624000000,
            "goodwill": 31885000000,
            "intangibleAssets": 0,
            "goodwillAndIntangibleAssets": 31885000000,
            "longTermInvestments": 0,
            "taxAssets": 17180000000,
            "otherNonCurrentAssets": 52856000000,
            "totalNonCurrentAssets": 286545000000,
            "otherAssets": 0,
            "totalAssets": 450256000000,
            "accountPayables": 7987000000,
            "shortTermDebt": 2887000000,
            "taxPayables": 8782000000,
            "deferredRevenue": 5036000000,
            "otherCurrentLiabilities": 64430000000,
            "totalCurrentLiabilities": 89122000000,
            "longTermDebt": 22574000000,
            "deferredRevenueNonCurrent": 0,
            "deferredTaxLiabilitiesNonCurrent": 0,
            "otherNonCurrentLiabilities": 13476000000,
            "totalNonCurrentLiabilities": 36050000000,
            "otherLiabilities": 0,
            "capitalLeaseObligations": 14578000000,
            "totalLiabilities": 125172000000,
            "preferredStock": 0,
            "commonStock": 0,
            "retainedEarnings": 245084000000,
            "accumulatedOtherComprehensiveIncomeLoss": -4800000000,
            "othertotalStockholdersEquity": 84800000000,
            "totalStockholdersEquity": 325084000000,
            "totalEquity": 325084000000,
            "totalLiabilitiesAndStockholdersEquity": 450256000000,
            "minorityInterest": 0,
            "totalLiabilitiesAndTotalEquity": 450256000000,
            "totalInvestments": 72191000000,
            "totalDebt": 25461000000,
            "netDebt": 1995000000,
            "link": "https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/0001652044-25-000014-index.htm",
            "finalLink": "https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm",
            "calculatedOtherCurrentAssets": 15714000000,
            "calculatedOtherNonCurrentAssets": 52856000000,
            "calculatedOtherCurrentLiabilities": 64430000000,
            "calculatedOtherNonCurrentLiabilities": -1102000000
        }}

        You will be given an array of balance sheets from different companies. Analyze each filing to extract valuable insights such as:
            - increasing/decreasing long-term liabilities/debt
            - increasing/decreasing cash and cash equivalents 
            - increasing/decreasing debt-to-equity ratios

        DON'T WRITE ANY CODE. Parse the given balance sheets.
        Each analysis must be a paragraph summarizing the pros and cons of the company.
        Output the analysis by company in the following format:
        {{
            'GOOG': ...
            'NVDA': ...
            ...
        }}

        GOOG:
        {self.balance_sheets["GOOG"]}

        NVDA:
        {self.balance_sheets["NVDA"]}

        META:
        {self.balance_sheets["META"]}

        MSFT:
        {self.balance_sheets["MSFT"]}

        TSLA:
        {self.balance_sheets["TSLA"]}

        AAPL:
        {self.balance_sheets["AAPL"]}

        AMZN:
        {self.balance_sheets["AMZN"]}
        """
        return prompt

    def query(self, prompt):
        return super().query(prompt)

    def get_analysis(self,):
        return self.query(self.generate_prompt())

if __name__ == "__main__":
    analyst = Analyst()
    pp.pprint(analyst.get_analysis())

