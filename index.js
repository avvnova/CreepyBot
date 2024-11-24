// Provides the necessary discord.js classes
const { Client, Collection, Events, GatewayIntentBits } = require('discord.js');
// Provides configuration variables
const { token, test, server } = require('./config.json');
// Provides utilities to interact with the file system
const fs = require('node:fs');
// Provides utilities to work with file and dir paths
const path = require('node:path');

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds] });
// Store and retrieve commands through a Collection, an extended Js map object
client.commands = new Collection();

// set the path for our commands and read the folders inside
const foldersPath = path.join(__dirName, 'commands');
const commandFolders = fs.readdirSync(foldersPath);

// for each folder in commands, build the folder's absolute path, and then get all the file names inside
for (const folder of commandFolders) {
    const commandsPath = path.join(foldersPath, folder);
    const commandFiles = fs.readdirSync(commandsPath).filter(file =>  file.endsWith('.js'));
    // for each file in the folder properties, validate it a bit, and add it to client.commands
    for (const file of commandFiles){
        const filePath = path.join(commandsPath, file);
        const command = require(filePath);
        // check file has data and execute properties, then add it with key-value pair <command_name, exported_module>
        if( 'data' in command && 'execute' in command) {
            client.commands.set(command.data.name, command);
        } else{
            console.log(`[WARNING] The command at ${filePath} is missing a required "data" or "execute" property.`);
        }
    }
}

// When the client is ready, run this code (only once).
// The distinction between `client: Client<boolean>` and `readyClient: Client<true>` is important for TypeScript developers.
// It makes some properties non-nullable.
client.once(Events.ClientReady, readyClient => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
});

// Log in to Discord with your client's token
client.login(token);
