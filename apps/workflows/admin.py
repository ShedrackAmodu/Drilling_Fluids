from django.contrib import admin
from .models import Workflow, Node, Edge

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('name', 'tenant', 'created_by', 'created_at')
    search_fields = ('name',)

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('workflow', 'node_type')

@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ('workflow', 'source', 'target')
