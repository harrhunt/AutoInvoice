from app import create_app
# noinspection PyPackageRequirements
import sass

sass.compile(dirname=('app/static/styles/sass', 'app/static/styles/css'), output_style='compressed')

app = create_app()
