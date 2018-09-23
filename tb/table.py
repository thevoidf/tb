from .item import Item


class Table:
	def __init__(self, header=None, rows=None):
		self.header = header
		self.rows = rows or []

		self.sep_char = '-'
		self.column_char = '|'
		self.corner_char = '+'

		self.fix_header()

	def get_column_length(self, n):
		rows_with_header = self.rows
		if self.header:
			rows_with_header = [self.header] + rows_with_header
		column = [row[n] for row in rows_with_header]
		return len(max(column, key=len))

	def separator(self):
		sep = self.corner_char
		columns = len(self.rows[0])

		for i in range(columns):
			sep += self.sep_char * (self.get_column_length(i) + 2) + self.corner_char
		return sep

	def fix_header(self):
		if self.header:
			if len(self.header) != len(self.rows[0]):
				for i in range(len(self.rows[0])):
					try:
						self.header[i]
					except:
						self.header.append('')
	
	def render(self):
		print(self)

	def __str__(self):
		self.fix_header()

		t = '\n'

		t += '{}\n'.format(self.separator())
		if self.header:
			for i, item in enumerate(self.header):
				column_length = self.get_column_length(i)
				t += str(Item(item, column_length, self.column_char))
			t += self.column_char + '\n{}\n'.format(self.separator())

		for row in self.rows:
			for i, item in enumerate(row):
				column_length = self.get_column_length(i)
				t += str(Item(item, column_length, self.column_char))
			t += self.column_char + '\n'

		t += '{}\n'.format(self.separator())
		return t

