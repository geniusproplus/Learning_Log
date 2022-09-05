"""让用户输入并提交信息的页面都是表单，那怕它看起来不像表单。用户输入信息时，我们需
要进行验证，确认提供的信息是正确的数据类型，且不是恶意的信息，如中断服务器的代码。然
后，我们再对这些有效信息进行处理，并将其保存到数据库的合适地方。这些工作很多都是由
Django自动完成的。

在Django中，创建表单的最简单方式是使用ModelForm，它根据我们在第18章定义的模型中
的信息自动创建表单。创建一个名为forms.py的文件，将其存储到models.py所在的目录中，并在
其中编写你的第一个表单"""

from django import forms
from .models import Entry, Topic

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']     
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        