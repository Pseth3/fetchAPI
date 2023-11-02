from flask import Flask, jsonify, request
import uuid
import json
import os
import math
import re


# Start the flask app
app = Flask(__name__)

# Make data store that contains all the receipts
allData = {}

# Check the format of the receipt received from the request
def checkReceipt(data):
    # Check if the receipt is valid
    # Return a boolean
    if set(['retailer', 'purchaseDate', 'purchaseTime', 'items', 'total'])!=set(data.keys()):
        return False
    if len(data['items'])<1:
        return False
    for item in data['items']:
        if set(item.keys())!=set(['shortDescription', 'price']):
            return False
        # Check for Regex patterns for list items
        list_patterns = {
        'shortDescription': "^[\\w\\s\\-]+$",
        'price': "\\d+\\.\\d{2}$"
        }
        for field, pattern in list_patterns.items():
            if field in item and not re.match(pattern, item[field]):
                return False

    # Check for Regex patterns
    patterns = {
        'retailer': "^\\S+$",
        'total': "^\\d+\\.\\d{2}$"
    }

    for field, pattern in patterns.items():
        if field in data and not re.match(pattern, data[field]):
            return False


    # Pass all checks
    return True

# Calculate the points based on rules
def calculatePoints(data):
    points = 0
    # Calculate the points

    # One point for every alphanumeric character in the retailer name.
    points += len([a for a in data["retailer"] if a.isalnum()])

    # 50 points if the total is a round dollar amount with no cents.
    if data["total"].split(".")[1]=="00":
        points += 50

    # 25 points if the total is a multiple of 0.25.
    if float(data["total"])%0.25==0:
        points += 25
    # 5 points for every two items on the receipt.
    points += len(data["items"])//2*5
    # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in data["items"]:
        if len(item["shortDescription"].strip())%3==0:
            points += math.ceil(float(item["price"])*0.2)
    # 6 points if the day in the purchase date is odd.
    if int(data["purchaseDate"].split("-")[2])%2==1:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    if int(data["purchaseTime"].split(":")[0])>14 and int(data["purchaseTime"].split(":")[0])<16:
        points += 10
    if int(data["purchaseTime"].split(":")[0])==14 and int(data["purchaseTime"].split(":")[0])<16 and int(data["purchaseTime"].split(":")[1])>0:
        points += 10
    
    return points





@app.route('/receipts/process',methods=['POST'])
def process_receipts():
    if request.method == 'POST':
        # Check if the body is json
        if not request.is_json:
            return "The receipt is invalid", 400

        # Get the json data from the request
        data = request.get_json()
        # Check the format
        if not checkReceipt(data):
            return  "The receipt is invalid", 400
        
        else:
            new_id = str(uuid.uuid1())
            data["points"] = calculatePoints(data)
            allData[new_id] = data

            return jsonify({'id': new_id}),200


@app.route('/receipts/<check_id>/points',methods=['GET'])
def get_points(check_id):
    if request.method == 'GET':
        # Check if request is valid

        # Check if the id exists
        if check_id not in allData.keys():
            return "No receipt found for that id",404
        else:
            # Calculate the points
            return jsonify({'points': allData[check_id]['points']}),200



# Start the main application
if __name__ == '__main__':

    app.run(debug=False,host='0.0.0.0')
