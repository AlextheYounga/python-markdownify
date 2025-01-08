from markdownify import markdownify as md


html = """
<article>
    <h1>Heading 1</h1>
    <div>
        <p>article body</p>
    </div>
    <article>
        <h2>Heading 2</h2>
        <div>
            <p>article body</p>
        </div>
    </article>
    <p>footnote</p>
</article>
"""

correct_conversion = """


Heading 1
=========

article body


Heading 2
---------

article body


footnote


"""


def test_newlines():
    assert md(html) == correct_conversion
