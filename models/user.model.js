const bcrypt = require('bcryptjs');
const db = require('../data/database');

class User {
    constructor(email, password, fullname, street, postal, city) {
        this.email = email,
        this.password = password,
        this.name = fullname,
        this.address = {
            street: street,
            postalCode: postal,
            city: city
        }
    };

    async signup() {
        const database = await db.connectDb();
        const hashedpassword = await bcrypt.hash(this.password, 12);
        database.query('insert into users (email, password, name, street, postal, city) values (\"' + this.email + '\", \"' + hashedpassword + '\", \"' + this.name + '\", \"' + this.address.street + '\", \"' + this.address.postalCode + '\", \"' + this.address.city + '\")');
    };
}

module.exports = User;