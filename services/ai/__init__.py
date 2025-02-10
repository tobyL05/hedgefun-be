import json
from services.agents.Investor import Investor
from services.agents.Analyst import Analyst

Buffet = Investor("Warren Buffet", 1000000, "A disciplined value investor seeking undervalued companies with strong fundamentals.", "Value", "Moderate", "P/E ratio below industry average and positive free cash flow.", "Stock price reaches target price or P/E ratio exceeds industry average.", "Formal and analytical", "Detailed explanations are required.")
Soros = Investor("George Soros", 1000000, "A global macro investor seeking to profit from market inefficiencies.", "Global Macro", "High", "Political and economic events that create opportunities.", "Market conditions change or geopolitical tensions escalate.", "Conversational and strategic", "High-level analysis is sufficient.")
Ackman = Investor("Bill Ackman", 1000000, "A contrarian investor focused on activist strategies and long-term value creation.", "Activist", "Moderate to High", "Undervalued companies with potential for strategic changes and strong brand equity.", "Target company achieves turnaround or valuation reaches fair value.", "Persuasive and analytical", "Moderate to detailed explanations are preferred.")
Burry = Investor("Michael Burry", 1000000, "A deep-value investor with a focus on identifying market bubbles and distressed assets.", "Deep Value", "High", "Severely mispriced assets, market inefficiencies, and asymmetric risk-reward opportunities.", "Market correction occurs or thesis is realized.", "Blunt and data-driven", "Highly detailed explanations are required.")
Hwang = Investor("Bill Hwang", 1000000, "A high-conviction investor leveraging significant leverage to build concentrated positions in growth stocks.", "High-Leverage Growth", "Very High", "High-growth companies with strong momentum and scalable business models.", "Forced liquidation, regulatory intervention, or fundamental thesis breakdown.", "Confident and faith-driven", "Moderate explanations with a focus on conviction over detailed analysis.")

def trade(role, funds, date):
    investor = None
    match role:
        case "warren_buffet":
            investor = Buffet
        case "bill_ackman":
            investor = Ackman
        case "george_soros":
            investor = Soros
        case "michael_burry":
            investor = Burry
        case "bill_hwang":
            investor = Hwang
        case _:
            return { "Error": "Bad Request"}, 400

    investor.set_fund(funds)

    res = investor.trade(funds, date)
    res = res[7:-3].strip()  # Remove ```json and ``` markers
    return json.loads(res)

            

