pipeline {
agent any

triggers {
// Ejecutar todos los días a las 21:00 (hora del servidor Jenkins)
cron('H 21 * * *')
}

stages {
stage('Checkout') {
steps {
echo 'Descargando código...'
checkout scm
}
}
  
stages {
stage('Preparar entorno') {
steps {
echo "Creando entorno virtual..."
bat '""C:\\Users\\anton\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"" -m venv venv'
bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
}
}

stage('Ejecutar script') {
steps {
echo "Generando reporte"
bat 'venv\\Scripts\\activate && python trabajoparcial.py'
}
}
}

stage('Pruebas') {
steps {
sh 'venv\\Scripts\\activate && python pruebas.py'
}
}

archiveArtifacts artifacts: 'reporte_*.txt', fingerprint: true
  
post {
success { echo "✅ Reporte de ventas generado exitosamente" }
failure { echo "❌ Error al generar reporte de ventas" }
}
}
