"""Protege somas entre lotes de processamento e a semântica de zero."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Dados' / '04_documentacao_e_auditoria'))
from atualizar_bases_tabnet import ler_lote, agregar_lotes


class AtualizacaoTabnetTest(unittest.TestCase):
    def lote(self, valores, total, ano):
        with tempfile.TemporaryDirectory() as tmp:
            csv = Path(tmp) / 'consulta.csv'
            html = Path(tmp) / 'consulta.html'
            csv.write_text('Consulta\n"UF";"2025/Nov";"2025/Dez";"Total"\n'
                           f'"14 Roraima";{valores};{total}\n'
                           f'"TOTAL";{valores};{total}\n', encoding='latin1')
            html.write_text('Legenda: - - Dado numérico igual a 0 não resultante de arredondamento.', encoding='latin1')
            return ler_lote(csv, html, ano)

    def test_lotes_sao_somados_pelo_atendimento_e_nao_substituidos(self):
        a = self.lote('1;-', 1, 2025)
        b = self.lote('17;14', 31, 2026)
        resultado = agregar_lotes([a, b], '2025-11', '2025-12')
        self.assertEqual(resultado['valor'].tolist(), [18, 14])
        self.assertEqual(resultado['ano_mes'].tolist(), ['2025-11', '2025-12'])

    def test_lote_repetido_nao_pode_duplicar_contagens(self):
        a = self.lote('1;2', 3, 2025)
        with self.assertRaises(ValueError):
            agregar_lotes([a, a], '2025-11', '2025-12')

    def test_celula_vazia_nao_vira_zero(self):
        with self.assertRaises(ValueError):
            self.lote('1;', 1, 2025)

    def test_total_inconsistente_interrompe_a_transformacao(self):
        with self.assertRaises(ValueError):
            self.lote('1;2', 4, 2025)

    def test_hifen_sem_legenda_confirmada_nao_vira_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            csv = Path(tmp) / 'c.csv'
            html = Path(tmp) / 'h.html'
            csv.write_text('"UF";"2025/Dez";"Total"\n"14 Roraima";-;0\n"TOTAL";-;0\n', encoding='latin1')
            html.write_text('Sem legenda', encoding='latin1')
            with self.assertRaises(ValueError):
                ler_lote(csv, html, 2025)


if __name__ == '__main__':
    unittest.main()
