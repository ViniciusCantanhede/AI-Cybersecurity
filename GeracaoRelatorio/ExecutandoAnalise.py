import subprocess 
import time

print(f"\nProjeto 4 - IA para Geração de Relatório de Segurança a Partir da Análise de Logs de Servidores Web\n")

def run_pipeline(script_name):
    try:
        result = subprocess.run(['python', script_name], check = True, capture_output = True, text = True)
        print(f"\nScript {script_name} executado com sucesso")
        print(f"\nSaída:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nErro ao executar o script {script_name}.")
        print(f"\nSaída de erro:\n{e.stderr}")
        return False

scripts = ['ValidaArquivo.py', 'AnalisaArquivo.py']

start_time = time.time()

for script in scripts:
    print(f"\nExecutando {script}...")
    success = run_pipeline(script)
    if not success:
        print(f"\nPipeline interrompido devido a falha na execução de {script}.")
        break

end_time = time.time()

execution_time = end_time - start_time

if success:
    print(f"\nPipeline concluído com sucesso em {execution_time:.2f} segundos.")
else:
    print(f"\nPipeline falhou após {execution_time:.2f} segundos.")