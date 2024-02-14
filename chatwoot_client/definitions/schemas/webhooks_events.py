""" 
Schemas for the webhook events.

Only implemented MessageCreatedEvent for now. Feel free to add more as needed.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List


@dataclass
class MessageCreatedEvent:
    account: Account
    additional_attributes: Any
    content_attributes: Any
    content_type: str
    content: str | None
    conversation: Conversation
    created_at: str
    id: int
    inbox: Inbox
    message_type: str
    private: bool
    sender: Sender
    source_id: Any | None
    attachments: List[Attachment] | None
    event: str


@dataclass
class Conversation:
    additional_attributes: Any
    can_reply: bool
    channel: str
    contact_inbox: ContactInbox
    id: int
    inbox_id: int
    messages: List[Message]
    labels: List[Any]
    meta: Meta
    status: str
    custom_attributes: Any
    snoozed_until: Any | None
    unread_count: int
    first_reply_created_at: None
    priority: Any | None
    waiting_since: int
    agent_last_seen_at: int
    contact_last_seen_at: int
    timestamp: int
    created_at: int


@dataclass
class ContactInbox:
    id: int
    contact_id: int
    inbox_id: int
    source_id: str
    created_at: str
    updated_at: str
    hmac_verified: bool
    pubsub_token: str


@dataclass
class Message:
    id: int
    content: str | None
    account_id: int
    inbox_id: int
    conversation_id: int
    message_type: int
    created_at: int
    updated_at: str
    private: bool
    status: str
    source_id: Any | None
    content_type: str
    content_attributes: Any
    sender_type: str
    sender_id: int
    external_source_ids: Any
    additional_attributes: Any
    processed_message_content: str | None
    sentiment: Any
    conversation: MessageConversation
    attachments: List[Attachment] | None
    sender: Sender


@dataclass
class MessageConversation:
    assignee_id: Any | None
    unread_count: int
    last_activity_at: int
    contact_inbox: ContactInbox


@dataclass
class ContactInbox:
    source_id: str


@dataclass
class Attachment:
    id: int
    message_id: int
    file_type: str
    account_id: int
    extension: Any | None
    data_url: str
    thumb_url: str
    file_size: int


@dataclass
class Meta:
    sender: Sender
    assignee: None
    team: None
    hmac_verified: bool


@dataclass
class Account:
    id: int
    name: str


@dataclass
class Inbox:
    id: int
    name: str


@dataclass
class Sender:
    account: Account | None
    additional_attributes: Any
    avatar: str | None
    custom_attributes: Any
    email: None
    id: int
    identifier: str
    name: str
    phone_number: str
    thumbnail: str
    type: str | None
