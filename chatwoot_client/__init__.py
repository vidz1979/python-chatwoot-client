from chatwoot_client.definitions.actions import *
from chatwoot_client.http import HttpClient
from chatwoot_client.definitions.schemas import input_schemas
from chatwoot_client.definitions.schemas import webhooks_events


class ChatwootClient:
    accounts: AccountsActions
    account_users: AccountUsersActions
    agent_bots: AgentBotsActions
    users: UsersActions
    account_agent_bots: AccountAgentBotsActions
    agents: AgentsActions
    canned_responses: CannedResponsesActions
    contacts: ContactsActions
    conversation_assignment: ConversationAssignmentActions
    conversation_labels: ConversationLabelsActions
    conversations: ConversationsActions
    custom_attributes: CustomAttributesActions
    custom_filters: CustomFiltersActions
    inboxes: InboxesActions
    integrations: IntegrationsActions
    messages: MessagesActions
    profile: ProfileActions
    reports: ReportsActions
    teams: TeamsActions
    webhooks: WebhooksActions
    automation_rules: AutomationRuleActions
    client_contacts: ClientContactsActions
    client_conversations: ClientConversationsActions
    client_messages: ClientMessagesActions

    def __init__(self, url, access_token):
        self.client = HttpClient(url, access_token)

        self.accounts = AccountsActions(self.client)
        self.account_users = AccountUsersActions(self.client)
        self.agent_bots = AgentBotsActions(self.client)
        self.users = UsersActions(self.client)
        self.account_agent_bots = AccountAgentBotsActions(self.client)
        self.agents = AgentsActions(self.client)
        self.canned_responses = CannedResponsesActions(self.client)
        self.contacts = ContactsActions(self.client)
        self.conversation_assignment = ConversationAssignmentActions(self.client)
        self.conversation_labels = ConversationLabelsActions(self.client)
        self.conversations = ConversationsActions(self.client)
        self.custom_attributes = CustomAttributesActions(self.client)
        self.custom_filters = CustomFiltersActions(self.client)
        self.inboxes = InboxesActions(self.client)
        self.integrations = IntegrationsActions(self.client)
        self.messages = MessagesActions(self.client)
        self.profile = ProfileActions(self.client)
        self.reports = ReportsActions(self.client)
        self.teams = TeamsActions(self.client)
        self.webhooks = WebhooksActions(self.client)
        self.automation_rules = AutomationRuleActions(self.client)
        self.client_contacts = ClientContactsActions(self.client)
        self.client_conversations = ClientConversationsActions(self.client)
        self.client_messages = ClientMessagesActions(self.client)
