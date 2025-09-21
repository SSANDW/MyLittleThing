const mysql = require('mysql2/promise');

async function connectDb() {
    const connection = await mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'skdml@100',
        database: 'myproject'
    });

    return connection;
};

module.exports = {
    connectDb: connectDb
};