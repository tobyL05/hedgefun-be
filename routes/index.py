from flask import Blueprint, request
from services.ai import trade

api_bp = Blueprint("api",__name__)

@api_bp.route("/initialize", methods=["POST"])
def init():
    print(request.args)
    return { "message": request.args }


@api_bp.route("/trade", methods=["GET"])
def generate():
    """
        This function will generate the trade based on given query param.
        Query params: {
            role: "warren_buffet" | "bill_ackman" | "george_soros" | "michael_burry"
        }
    """
    params = request.args
    role = params["role"]
    funds = params["funds"]
    return trade(role, funds)
