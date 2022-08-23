from django.db import models

# Create your models here.
from django.db.models.fields import related


class Tickets(models.Model):
    url = models.CharField(max_length=256, blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True)
    via = models.TextField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=256, blank=True, null=True)
    subject = models.TextField(max_length=256, blank=True, null=True)
    raw_subject = models.TextField(max_length=612, blank=True, null=True)
    description = models.TextField(max_length=1224, blank=True, null=True)
    priority = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=256, blank=True, null=True)
    recipient = models.CharField(max_length=1224, blank=True, null=True)
    requester_id = models.IntegerField(blank=True, null=True)
    submitter_id = models.IntegerField(blank=True, null=True)
    assignee_id = models.IntegerField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    collaborator_ids = models.CharField(max_length=256, blank=True, null=True)
    follower_ids = models.CharField(max_length=256, blank=True, null=True)
    email_cc_ids = models.CharField(max_length=256, blank=True, null=True)
    forum_topic_id = models.IntegerField(blank=True, null=True)
    problem_id = models.IntegerField(blank=True, null=True)
    has_incidents = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    due_at = models.DateTimeField(blank=True, null=True)
    tags = models.CharField(max_length=1224, blank=True, null=True)
    custom_fields = models.CharField(max_length=1224, blank=True, null=True)
    satisfaction_rating = models.FloatField(blank=True, null=True)
    sharing_agreement_ids = models.CharField(max_length=1224, blank=True, null=True)
    fields = models.CharField(max_length=1224, blank=True, null=True)
    followup_ids = models.CharField(max_length=1224, blank=True, null=True)
    ticket_form_id = models.IntegerField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    allow_channelback = models.BooleanField(default=False)
    allow_attachments = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"ID: {self.pk} - Subject:{self.subject}"


class Comments(models.Model):
    ticket = models.ForeignKey(Tickets, models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    html_body = models.TextField(blank=True, null=True)
    plain_body = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=False)
    attachments = models.CharField(max_length=512, blank=True, null=True)
    audit_id = models.IntegerField(blank=True, null=True)
    via = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"ID: {self.pk} - Ticket ID: {self.ticket.id} - Plain body: {self.plain_body}"
