""" All actions for resources are defined here. """

from chatwoot_client.action import Actions

from .schemas.input_schemas import *


class AccountsActions(Actions):
    def create(self, payload: AccountCreateUpdatePayload):
        return self.client.post("platform/api/v1/accounts", data=payload)

    def get(self, account_id: int):
        return self.client.get(f"platform/api/v1/accounts/{account_id}")

    def update(self, account_id: int, payload: AccountCreateUpdatePayload):
        return self.client.patch(f"platform/api/v1/accounts/{account_id}", data=payload)

    def delete(self, account_id: int):
        return self.client.delete(f"platform/api/v1/accounts/{account_id}")


class AccountUsersActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"platform/api/v1/accounts/{account_id}/account_users")

    def create(self, account_id: int, payload: PlatformApiV1AccountsAccountIdAccountUsersPostRequest):
        return self.client.post(f"platform/api/v1/accounts/{account_id}/account_users", data=payload)

    def delete(self, account_id: int, account_user_id: int):
        return self.client.delete(f"platform/api/v1/accounts/{account_id}/account_users/{account_user_id}")


class AgentBotsActions(Actions):
    def list(self):
        return self.client.get("platform/api/v1/agent_bots")

    def create(self, payload: AgentBotCreateUpdatePayload):
        return self.client.post("platform/api/v1/agent_bots", data=payload)

    def get(self, id: int):
        return self.client.get(f"platform/api/v1/agent_bots/{id}")

    def update(self, id: int, payload: AgentBotCreateUpdatePayload):
        return self.client.patch(f"platform/api/v1/agent_bots/{id}", data=payload)

    def delete(self, id: int):
        return self.client.delete(f"platform/api/v1/agent_bots/{id}")


class UsersActions(Actions):
    def list(self):
        return self.client.get("platform/api/v1/users")

    def create(self, payload: UserCreateUpdatePayload):
        return self.client.post("platform/api/v1/users", data=payload)

    def get(self, id: int):
        return self.client.get(f"platform/api/v1/users/{id}")

    def update(self, id: int, payload: UserCreateUpdatePayload):
        return self.client.patch(f"platform/api/v1/users/{id}", data=payload)

    def delete(self, id: int):
        return self.client.delete(f"platform/api/v1/users/{id}")

    def get_sso_link(self, id: int):
        return self.client.get(f"platform/api/v1/users/{id}/login")


class AccountAgentBotsActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/agent_bots")

    def create(self, account_id: int, payload: AgentBotCreateUpdatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/agent_bots", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/agent_bots/{id}")

    def get(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/agent_bots/{id}")

    def update(self, account_id: int, id: int, payload: AgentBotCreateUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/agent_bots/{id}", data=payload)


class AgentsActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/agents")

    def create(self, account_id: int, payload: ApiV1AccountsAccountIdAgentsPostRequest):
        return self.client.post(f"api/v1/accounts/{account_id}/agents", data=payload)

    def update(self, account_id: int, id: int, payload: ApiV1AccountsAccountIdAgentsIdPatchRequest):
        return self.client.patch(f"api/v1/accounts/{account_id}/agents/{id}", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/agents/{id}")


class CannedResponsesActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/canned_responses")

    def create(self, account_id: int, payload: CannedResponseCreateUpdatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/canned_responses", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/canned_responses/{id}")


class ContactsActions(Actions):
    def list(self, account_id: int, query: ApiV1AccountsAccountIdContactsGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/contacts", query=query)

    def create(self, account_id: int, payload: ContactCreate):
        return self.client.post(f"api/v1/accounts/{account_id}/contacts", data=payload)

    def update(self, account_id: int, id: int, payload: ContactUpdate):
        return self.client.patch(f"api/v1/accounts/{account_id}/contacts/{id}", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/contacts/{id}")

    def get(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/contacts/{id}")

    def get_conversations(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/contacts/{id}/conversations")

    def search(self, account_id: int, query: ApiV1AccountsAccountIdContactsSearchGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/contacts/search", query=query)

    def filter(
        self,
        account_id: int,
        query: ApiV1AccountsAccountIdContactsFilterPostParametersQuery,
        payload: ApiV1AccountsAccountIdContactsFilterPostRequest,
    ):
        return self.client.post(f"api/v1/accounts/{account_id}/contacts/filter", query=query, data=payload)


class ConversationAssignmentActions(Actions):
    def assign(
        self,
        account_id: int,
        conversation_id: int,
        payload: ApiV1AccountsAccountIdConversationsConversationIdAssignmentsPostRequest,
    ):
        return self.client.post(
            f"api/v1/accounts/{account_id}/conversations/{conversation_id}/assignments", data=payload
        )


class ConversationLabelsActions(Actions):
    def list(self, account_id: int, conversation_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/labels")

    def create(
        self,
        account_id: int,
        conversation_id: int,
        payload: ApiV1AccountsAccountIdConversationsConversationIdLabelsPostRequest,
    ):
        return self.client.post(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/labels", data=payload)


class ConversationsActions(Actions):
    def get_meta(self, account_id: int, query: ApiV1AccountsAccountIdConversationsMetaGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/conversations/meta", query=query)

    def list(self, account_id: int, query: ApiV1AccountsAccountIdConversationsGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/conversations", query=query)

    def create(self, account_id: int, payload: ApiV1AccountsAccountIdConversationsPostRequest):
        return self.client.post(f"api/v1/accounts/{account_id}/conversations", data=payload)

    def get(self, account_id: int, conversation_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/conversations/{conversation_id}")

    def filter(
        self,
        account_id: int,
        query: ApiV1AccountsAccountIdConversationsFilterPostParametersQuery,
        payload: ApiV1AccountsAccountIdConversationsFilterPostRequest,
    ):
        return self.client.post(f"api/v1/accounts/{account_id}/conversations/filter", query=query, data=payload)

    def toggle_status(self, account_id: int, conversation_id: int):
        return self.client.post(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status")


class CustomAttributesActions(Actions):
    def list(self, account_id: int, query: ApiV1AccountsAccountIdCustomAttributeDefinitionsGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/custom_attribute_definitions", query=query)

    def create(self, account_id: int, payload: CustomAttributeCreateUpdatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/custom_attribute_definitions", data=payload)

    def get(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/custom_attribute_definitions/{id}")

    def update(self, account_id: int, id: int, payload: CustomAttributeCreateUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/custom_attribute_definitions/{id}", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/custom_attribute_definitions/{id}")


class CustomFiltersActions(Actions):
    def list(self, account_id: int, query: ApiV1AccountsAccountIdCustomFiltersGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/custom_filters", query=query)

    def create(
        self,
        account_id: int,
        query: ApiV1AccountsAccountIdCustomFiltersPostParametersQuery,
        payload: CustomFilterCreateUpdatePayload,
    ):
        return self.client.post(f"api/v1/accounts/{account_id}/custom_filters", query=query, data=payload)

    def get(self, account_id: int, custom_filter_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}")

    def update(self, account_id: int, custom_filter_id: int, payload: CustomFilterCreateUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}", data=payload)

    def delete(self, account_id: int, custom_filter_id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/custom_filters/{custom_filter_id}")


class InboxesActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/inboxes")

    def create(self, account_id: int, payload: ApiV1AccountsAccountIdInboxesPostRequest):
        return self.client.post(f"api/v1/accounts/{account_id}/inboxes", data=payload)

    def get(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/inboxes/{id}")

    def update(self, account_id: int, id: int, payload: ApiV1AccountsAccountIdInboxesIdPatchRequest):
        return self.client.patch(f"api/v1/accounts/{account_id}/inboxes/{id}", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/inboxes/{id}")

    def get_associated_agent_bot(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/inboxes/{id}/agent_bot")

    def set_agent_bot(self, account_id: int, id: int, payload: ApiV1AccountsAccountIdInboxesIdSetAgentBotPostRequest):
        return self.client.post(f"api/v1/accounts/{account_id}/inboxes/{id}/set_agent_bot", data=payload)

    def list_agents(self, account_id: int, inbox_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/inbox_members/{inbox_id}")

    def delete_agent(
        self, account_id: int, inbox_id: int, payload: ApiV1AccountsAccountIdInboxMembersInboxIdDeleteRequest
    ):
        return self.client.delete(f"api/v1/accounts/{account_id}/inbox_members/{inbox_id}", data=payload)

    def add_agent(self, account_id: int, payload: ApiV1AccountsAccountIdInboxMembersPostRequest):
        return self.client.post(f"api/v1/accounts/{account_id}/inbox_members", data=payload)

    def update_agent(self, account_id: int, payload: ApiV1AccountsAccountIdInboxMembersPatchRequest):
        return self.client.patch(f"api/v1/accounts/{account_id}/inbox_members", data=payload)


class IntegrationsActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/integrations/apps")

    def create(self, account_id: int, payload: IntegrationsHookCreatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/integrations/hooks", data=payload)

    def update(self, account_id: int, hook_id: int, payload: IntegrationsHookUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/integrations/hooks/{hook_id}", data=payload)

    def delete(self, account_id: int, hook_id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/integrations/hooks/{hook_id}")


class MessagesActions(Actions):
    def list(self, account_id: int, conversation_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/messages")

    def create(self, account_id: int, conversation_id: int, payload: ConversationMessageCreate):
        return self.client.post(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/messages", data=payload)

    def delete(self, account_id: int, conversation_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/messages/{id}")

    def create_attachment(self, account_id: int, conversation_id: int, payload: ConversationMessageAttachmentCreate):
        return self.client.post(f"api/v1/accounts/{account_id}/conversations/{conversation_id}/messages", data=payload)


class ProfileActions(Actions):
    def get(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/profile")


class ReportsActions(Actions):
    def get_accounts_report(self, account_id: int, query: ApiV2AccountsAccountIdReportsGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/reports", query=query)

    def get_account_report_summary(
        self, account_id: int, query: ApiV2AccountsAccountIdReportsSummaryGetParametersQuery
    ):
        return self.client.get(f"api/v1/accounts/{account_id}/reports/summary", query=query)

    def get_conversation_metrics_for_account(
        self, account_id: int, query: ApiV2AccountsAccountIdReportsConversationsGetParametersQuery
    ):
        return self.client.get(f"api/v1/accounts/{account_id}/reports/conversations", query=query)

    def get_conversation_metrics_for_agent(
        self, account_id: int, query: ApiV2AccountsAccountIdReportsConversationsGetParametersQuery1
    ):
        return self.client.get(f"api/v1/accounts/{account_id}/reports/conversations", query=query)


class TeamsActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/teams")

    def create(self, account_id: int, payload: TeamCreateUpdatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/teams", data=payload)

    def get(self, account_id: int, team_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/teams/{team_id}")

    def update(self, account_id: int, team_id: int, payload: TeamCreateUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/teams/{team_id}", data=payload)

    def delete(self, account_id: int, team_id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/teams/{team_id}")

    def list_agents(self, account_id: int, team_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/teams/{team_id}/team_members")

    def delete_agent(
        self, account_id: int, team_id: int, payload: AccountsAccountIdTeamsTeamIdTeamMembersDeleteRequest
    ):
        return self.client.delete(f"api/v1/accounts/{account_id}/teams/{team_id}/team_members", data=payload)

    def add_agent(self, account_id: int, team_id: int, payload: AccountsAccountIdTeamsTeamIdTeamMembersPostRequest):
        return self.client.post(f"api/v1/accounts/{account_id}/teams/{team_id}/team_members", data=payload)

    def update_agent(self, account_id: int, team_id: int, payload: AccountsAccountIdTeamsTeamIdTeamMembersPatchRequest):
        return self.client.patch(f"api/v1/accounts/{account_id}/teams/{team_id}/team_members", data=payload)


class WebhooksActions(Actions):
    def list(self, account_id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/webhooks")

    def create(self, account_id: int, payload: WebhookCreateUpdatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/webhooks", data=payload)

    def update(self, account_id: int, webhook_id: int, payload: WebhookCreateUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/webhooks/{webhook_id}", data=payload)

    def delete(self, account_id: int, webhook_id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/webhooks/{webhook_id}")


class AutomationRuleActions(Actions):
    def list(self, account_id: int, query: ApiV1AccountsAccountIdAutomationRulesGetParametersQuery):
        return self.client.get(f"api/v1/accounts/{account_id}/automation_rules", query=query)

    def create(self, account_id: int, payload: AutomationRuleCreateUpdatePayload):
        return self.client.post(f"api/v1/accounts/{account_id}/automation_rules", data=payload)

    def get(self, account_id: int, id: int):
        return self.client.get(f"api/v1/accounts/{account_id}/automation_rules/{id}")

    def update(self, account_id: int, id: int, payload: AutomationRuleCreateUpdatePayload):
        return self.client.patch(f"api/v1/accounts/{account_id}/automation_rules/{id}", data=payload)

    def delete(self, account_id: int, id: int):
        return self.client.delete(f"api/v1/accounts/{account_id}/automation_rules/{id}")


class ClientContactsActions(Actions):
    def create(self, inbox_identifier: int, payload: PublicContactCreateUpdatePayload):
        return self.client.post(f"public/api/v1/inboxes/{inbox_identifier}/contacts", data=payload)

    def get(self, inbox_identifier: int, contact_identifier: int):
        return self.client.get(f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}")

    def update(self, inbox_identifier: int, contact_identifier: int, payload: PublicContactCreateUpdatePayload):
        return self.client.patch(
            f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}", data=payload
        )


class ClientConversationsActions(Actions):
    def list(self, inbox_identifier: int, contact_identifier: int):
        return self.client.get(f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations")

    def create(self, inbox_identifier: int, contact_identifier: int):
        return self.client.post(f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations")


class ClientMessagesActions(Actions):
    def list(self, inbox_identifier: int, contact_identifier: int, conversation_id: int):
        return self.client.get(
            f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages"
        )

    def create(
        self,
        inbox_identifier: int,
        contact_identifier: int,
        conversation_id: int,
        payload: PublicMessageCreatePayload,
    ):
        return self.client.post(
            f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages",
            data=payload,
        )

    def update(
        self,
        inbox_identifier: int,
        contact_identifier: int,
        conversation_id: int,
        message_id: int,
        payload: PublicMessageUpdatePayload,
    ):
        return self.client.patch(
            f"public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages/{message_id}",
            data=payload,
        )
