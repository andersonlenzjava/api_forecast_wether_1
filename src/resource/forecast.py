from flask import Flask, make_response, jsonify, request
from flask_restx import fields, Api, Resource, Namespace, reqparse
from flask_cors import CORS

from src.utils.response import Response

from src.service.Accu_Wheater_Forecast.city_days_forecast import cityDaysForecast

path_variable = reqparse.RequestParser()
path_variable.add_argument("city", type=str, default="Cascavel", required=True)
path_variable.add_argument("state", type=str, default="Parana", required=True)
path_variable.add_argument("days", type=int, default=1, required=True)

forecast_ns = Namespace("api")

@forecast_ns.route("/forecast")
class Forecast(Resource):

    forecast_ns.expect(path_variable, validate=True)
    def get(self):

        # Ocorreu um erro: list index out of range --> é por que as vezes só vem o dia, nao a noite

        try:            
            city = request.headers.get("city")
            state = request.headers.get("state")
            days = int(request.headers.get("days", 1))
            
            forecast = cityDaysForecast().daysForecast(city=city, state=state, days=days)
            
            return Response().response(
                status_code=200, 
                message_id="Get forecast sucess", 
                data=forecast
            )
        except Exception as e:
            return Response().response(status_code=400, error=True, message_id="bad_request", exception=str(e))
  
