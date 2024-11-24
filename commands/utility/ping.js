const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('ping')
        .setDescription('Replies with "Pong!" and a latency metric. Used for latency and liveness testing of bot'),
    async execute(interaction) {
        const sent = await interaction.reply({content: '*Ping . . .*', fetchReply: true });
        interaction.editReply(`***Pong!***    Roundtrip latency: ${sent.createdTimestamp - interaction.createdTimestamp}ms`)
    },
};