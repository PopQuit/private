reaction_logger = {
    "added": {
        "title": "Emoji added:",
        "content": "User: {member.mention} (`{member.id}`)\n"
                   "Channel: {channel.mention} (`{channel.id}`)\n"
                   "Emoji: {emoji.name}\n",
        "footer": {
            "text": "Emoji Logger",
            "icon": "{guild.icon_url}",
            "timestamp": True
        },
        "color": {
            "random": False,
            "color": 0x00ff00
        }
    },
    "removed": {
        "title": "Emoji removed:",
        "content": "User: {member.mention} (`{member.id}`)\n"
                   "Channel: {channel.mention} (`{channel.id}`)\n"
                   "Emoji: {emoji.name}\n",
        "footer": {
            "text": "Emoji Logger",
            "icon": "{guild.icon_url}",
            "timestamp": True
        },
        "color": {
            "random": False,
            "color": 0xff0000
        }
    }
}
role_notifier = {
    "added": {
        "title": "Role received!",
        "content": "You have received the **{role.name}** role in {guild.name}!",
        "footer": {
            "text": "Role Notifier",
            "icon": "{guild.icon_url}",
            "timestamp": True
        },
        "color": {
            "random": False,
            "color": 0x00ff00
        }
    },
    "removed": {
        "title": "Role removed!",
        "content": "The **{role.name}** role in {guild.name} has been removed from you!",
        "footer": {
            "text": "Role Notifier",
            "icon": "{guild.icon_url}",
            "timestamp": True
        },
        "color": {
            "random": False,
            "color": 0xff0000
        }
    }
}
