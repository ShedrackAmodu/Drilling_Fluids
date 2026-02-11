# Visualization helpers: produce chart payloads for front-end charting libs
from apps.visualization.models import ChartWidget

class VisualizationService:
    @staticmethod
    def render_chart(widget: ChartWidget):
        # Placeholder: translate widget.query/options into chart data
        # Frontend should use Plotly/Chart.js; this returns data + layout
        return {
            'data': [],
            'layout': {},
            'meta': {'title': widget.title}
        }
