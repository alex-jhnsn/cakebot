const Database = require("./Database");
const queryString = require("query-string");

var database = new Database();

exports.handle = async (event, context) => {

    //Allow for other people to delete bakers by passing in a message with their name or something, 
    //change return message appropriately

    let userId;

    try {
        let body = queryString.parse(event.body);
        userId = body.user_id;
        console.log(userId);
    } catch (error) {
        return (null, {statusCode: 400, body: "Missing user id."});
    }

    if(await database.deleteBaker(userId))
        return (null, {statusCode: 200, body: "You are no longer a baker."});
    
    return (null, {statusCode: 500, body: "Oops, there was an error. Please try again"});
}