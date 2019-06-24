const Database = require("./Database");
const queryString = require("query-string");

var database = new Database();

exports.handle = async (event, context) => {
    let userId;
    
    try {
        let body = queryString.parse(event.body);
        console.log(body);
        userId = body.user_id;
        console.log("User Id = " + userId);
    } catch (error) {
        return (null, {statusCode: 400, body: "Missing user id."});
    }

    //If user already exists return that.

    if (await database.addBaker(userId))
        return (null, {statusCode: 200, body: "You are now a baker!"});
    
    return (null, {statusCode: 200, body: "Oops, there was an error. Please try again"});
}