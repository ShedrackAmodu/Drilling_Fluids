from django.db import models
from apps.users.models import User
from apps.core.models import Tenant

class Workflow(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Node(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='nodes')
    node_type = models.CharField(max_length=50, choices=[('input','Input'),('calculation','Calculation'),('visualization','Visualization'),('report','Report')])
    config = models.JSONField(blank=True, null=True)
    position = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.workflow.name} - {self.node_type} ({self.id})"

class Edge(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='edges')
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outgoing')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='incoming')
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.workflow.name} edge {self.source.id} -> {self.target.id}"
