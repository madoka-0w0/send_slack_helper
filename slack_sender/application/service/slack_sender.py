import slackweb

from slack_sender.application.model.slack_message import SlackMessage


class SlackSender:

    def send(self, slack_url, message: SlackMessage):
        payload = {
            "text": message.message,
            "unfurl_links": message.unfurl_links,
            "channel": message.channel,
            "username": message.user_name
        }

        slackweb.Slack(slack_url).send(payload=payload)
