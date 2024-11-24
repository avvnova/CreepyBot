const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('user')
        .setDescription('Provides user info.'),
    async execute(interaction) {
        // interaction.user is the object representing the user running the command
        // interaction.member is the object representing the target user of the command
        await interaction.reply(`This command was run by ${interaction.user.username}, who joined on ${interaction,member.joinedAt}.`);
     },
};