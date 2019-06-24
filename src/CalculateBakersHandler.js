const Database = require("./Database");

const config = require('./config.json');
global.gConfig = config;

exports.handle = function() {
    let requiredBakers = global.gConfig.numberOfBakersRequired;
    console.log("Getting " + requiredBakers + " bakers.");

    return (null, {statusCode: 200, body: requiredBakers});
}