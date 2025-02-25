"""
main.py

Главный модуль приложения. Управляет взаимодействием всех модулей,
инициализирует API и предоставляет интерфейс для пользователя.
"""

from network.structure import UXAnalyzer
from interface.frontend import start_frontend
from interface.dashboard import Dashboard
from interface.report import ReportGenerator
from analysis.backend import Backend
from analysis.parsing import Parser
from analysis.services import ExternalServices
from analysis.recommendations import RecommendationEngine

def start_services():
    """
    Инициализирует все модули системы.
    """
    global backend, parser, services, recommender, dashboard, reporter, analyzer
    backend = Backend()
    parser = Parser()
    services = ExternalServices()
    recommender = RecommendationEngine()
    dashboard = Dashboard()
    reporter = ReportGenerator()
    analyzer = UXAnalyzer()

def run_analysis(url):
    """
    Выполняет анализ сайта и формирует рекомендации.

    :param url: URL анализируемого сайта.
    """
    html = parser.fetch_html(url)
    content = parser.parse_content(html)
    analytics = services.fetch_analytics("site_id")
    recommendations = recommender.generate_recommendations(content)
    dashboard.display_metrics(analytics)
    reporter.generate_pdf(recommendations)

def main():
    """
    Основная точка входа в приложение.
    """
    start_services()
    data = "current user"
    analyzer.analyze_user_behavior(data)
    start_frontend()

if __name__ == "__main__":
    main()
