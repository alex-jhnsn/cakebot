const tableName = "cakebot-BakersTable-ZYE2WB2BF2J9";
const AWS = require("aws-sdk");

module.exports = class Database {

    constructor() {
        AWS.config.update({
            region: "eu-west-1",
            //endpoint: "http://localhost:8000"
        });

        this.docClient = new AWS.DynamoDB.DocumentClient({apiVersion: '2012-08-10'});
    }

    async addBaker(userId) {
        var params = {
            TableName: tableName,
            Item: {
                "UserId": userId,
                "TimesBaked": 0,
                "LastBaked": new Date(2019, 6, 1).toJSON(),
                "Available": "true",
                "Baking": "false"
            }
        };
        
        try {
            await this.docClient.put(params).promise();
        } catch (error) {
            console.error("Unable to add baker. Error JSON:", JSON.stringify(error, null, 2));
            return false;
        }

        console.log("Added baker with Id: " + userId);
        return true;
    }
    
    async deleteBaker(userId) {
        var params = {
            TableName: tableName,
            Key: {
                "UserId": userId
            }
        };
        
        console.log("Deleting baker");

        try {
            await this.docClient.delete(params).promise();
        } catch (error) {
            console.error("Unable to delete baker. Error JSON:", JSON.stringify(err, null, 2));
            return false;
        }

        console.log("Deleted baker with Id: " + userId);
        return true;
    }
}